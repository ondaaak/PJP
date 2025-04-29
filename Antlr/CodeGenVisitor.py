from ExprVisitor import ExprVisitor

class CodeGenVisitor(ExprVisitor):
    def __init__(self):
        self.code = []
        self.label_counter = -1  # Inicializovat na -1
        self.var_types = {}

    def new_label(self):
        self.label_counter += 1
        return self.label_counter

    def visitProg(self, ctx):
        for cmd in ctx.command():
            self.visit(cmd)
        return self.code

    def visitExprStatement(self, ctx):
        self.visit(ctx.expr())
        self.code.append("pop")  # zahodí výsledek výrazu

    def visitDeclaration(self, ctx):
        print("DEBUG: visitDeclaration called")
        type_name = self.visit(ctx.type_())
        print(f"DEBUG: type_name = {type_name}")
        
        # Přístup ke všem ID tokenům
        id_list = ctx.ID()
        for id_token in id_list:
            var_name = id_token.getText()
            print(f"DEBUG: var_name = {var_name}")
            self.var_types[var_name] = type_name
            
            # Přidej výchozí hodnoty podle typu
            if type_name == 'int':
                print("DEBUG: Adding push I 0")
                self.code.append("push I 0")
            elif type_name == 'float':
                self.code.append("push F 0.0")
            elif type_name == 'bool':
                self.code.append("push B false")
            elif type_name == 'string':
                self.code.append("push S \"\"")
            elif type_name == 'FILE':
                self.code.append("push S \"\"")
        
            # Ulož výchozí hodnotu do proměnné
            self.code.append(f"save {var_name}")

    def visitDeclarationWithAssignment(self, ctx):
        var_name = ctx.ID().getText()
        # Získej typ z kontextu
        type_name = self.visit(ctx.type_())
        # Zaznamenej typ proměnné
        self.var_types[var_name] = type_name
        # Vygeneruj kód pro výraz a uložení
        self.visit(ctx.expr())
        self.code.append(f"save {var_name}")

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.visit(ctx.expr())
        self.code.append(f"save {var_name}")
        self.code.append(f"load {var_name}")  # Přidej načtení hodnoty po přiřazení

    def visitIntLiteral(self, ctx):
        value = ctx.INT().getText()
        self.code.append(f"push I {value}")

    def visitFloatLiteral(self, ctx):
        value = ctx.FLOAT().getText()
        self.code.append(f"push F {value}")

    def visitStringLiteral(self, ctx):
        value = ctx.STRING().getText()
        self.code.append(f"push S {value}")

    def visitBoolLiteral(self, ctx):
        value = ctx.BOOL().getText()
        self.code.append(f"push B {value}")

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        self.code.append(f"load {var_name}")

    def visitAddSubConcat(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            # Zjisti typ (I nebo F) podle typu operandů, zde zjednodušeně I
            self.code.append("add I")
        elif op == '-':
            self.code.append("sub I")
        elif op == '.':
            self.code.append("concat")
    
    def visitMulDivMod(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            self.code.append("mul I")  # nebo "mul F" podle typu
        elif op == '/':
            self.code.append("div I")  # nebo "div F" podle typu
        elif op == '%':
            self.code.append("mod")
            
    def visitLogicalAnd(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("and")

    def visitLogicalOr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.code.append("or")

    def visitLogicalNot(self, ctx):
        self.visit(ctx.expr())
        self.code.append("not")

    def visitRelational(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)

        self.visit(left_ctx)
        if left_type == 'int' and right_type == 'float':
            self.code.append("itof")
        self.visit(right_ctx)
        if right_type == 'int' and left_type == 'float':
            self.code.append("itof")

        op = ctx.getChild(1).getText()
        if op == '<':
            if left_type == 'float' or right_type == 'float':
                self.code.append("lt F")
            else:
                self.code.append("lt I")
        elif op == '>':
            if left_type == 'float' or right_type == 'float':
                self.code.append("gt F")
            else:
                self.code.append("gt I")
        # ... další operátory ...

    def visitEquality(self, ctx):
        left_ctx = ctx.expr(0)
        right_ctx = ctx.expr(1)
        
        # Zjisti typy operandů
        left_type = self.getExprType(left_ctx)
        right_type = self.getExprType(right_ctx)
        
        # Navštiv oba výrazy, aby se jejich hodnoty dostaly na zásobník
        self.visit(left_ctx)
        self.visit(right_ctx)
        
        # Zvol správnou instrukci podle typu operandů
        op = ctx.getChild(1).getText()  # == nebo !=
        
        # Zjisti, jaký typ rovnosti použít
        eq_type = "I"  # výchozí typ je int
        if left_type == 'string' or right_type == 'string':
            eq_type = "S"
        elif left_type == 'float' or right_type == 'float':
            eq_type = "F"
        
        # Generuj instrukci eq s odpovídajícím typem
        self.code.append(f"eq {eq_type}")
        
        # Pro != potřebujeme negovat výsledek
        if op == '!=':
            self.code.append("not")

    def visitUnaryMinus(self, ctx):
        self.visit(ctx.expr())
        self.code.append("uminus I")  # nebo "uminus F" podle typu

    def visitItf(self, ctx):
        self.visit(ctx.expr())
        self.code.append("itof")

    def visitWriteStatement(self, ctx):
        n = len(ctx.expr())
        for expr_ctx in ctx.expr():
            self.visit(expr_ctx)
        self.code.append(f"print {n}")

    def getExprType(self, ctx):
        # Zjednodušeně: podle typu uzlu
        if hasattr(ctx, 'INT'):
            return 'int'
        if hasattr(ctx, 'FLOAT'):
            return 'float'
        if hasattr(ctx, 'STRING'):
            return 'string'
        if hasattr(ctx, 'BOOL'):
            return 'bool'
        # Pokud je to proměnná, vrať typ proměnné (musíš mít slovník typů)
        if hasattr(ctx, 'ID'):
            var_name = ctx.ID().getText()
            return self.var_types.get(var_name, None)
        # Doplň další podle potřeby
        return None

    def visitWhileStatement(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()
        
        # Label na začátek cyklu
        self.code.append(f"label {start_label}")
        
        # Podmínka cyklu
        self.visit(ctx.expr())
        
        # Pokud je podmínka false, skoč na konec cyklu
        self.code.append(f"fjmp {end_label}")
        
        # Tělo cyklu
        self.visit(ctx.statement())
        
        # Skok zpět na začátek cyklu
        self.code.append(f"jmp {start_label}")
        
        # Label pro konec cyklu
        self.code.append(f"label {end_label}")

    def visitIfStatement(self, ctx):
        end_label = self.new_label()
        
        # Vyhodnoť podmínku
        self.visit(ctx.expr())
        
        # Pokud je podmínka false, skoč na konec
        self.code.append(f"fjmp {end_label}")
        
        # Tělo if
        self.visit(ctx.statement())
        
        # Po dokončení if bloku skoč za konec
        next_label = self.new_label()
        self.code.append(f"jmp {next_label}")
        
        # Label pro konec if (když je podmínka false)
        self.code.append(f"label {end_label}")
        
        # Label pro následující kód
        self.code.append(f"label {next_label}")

    def visitIfElseStatement(self, ctx):
        else_label = self.new_label()
        end_label = self.new_label()
        
        # Vyhodnoť podmínku
        self.visit(ctx.expr())
        
        # Pokud je podmínka false, skoč na else větev
        self.code.append(f"fjmp {else_label}")
        
        # Tělo if
        self.visit(ctx.statement(0))
        
        # Po skončení if bloku skoč na konec celé konstrukce
        self.code.append(f"jmp {end_label}")
        
        # Label pro else část
        self.code.append(f"label {else_label}")
        
        # Else větev
        self.visit(ctx.statement(1))
        
        # Label pro konec celé if/else konstrukce
        self.code.append(f"label {end_label}")

    def visitReadStatement(self, ctx):
        for id_ctx in ctx.ID():
            var_name = id_ctx.getText()
            # Zjisti typ proměnné (musíš mít slovník typů, např. self.var_types)
            typ = self.var_types.get(var_name, None)
            if typ == 'int':
                self.code.append("read I")
            elif typ == 'float':
                self.code.append("read F")
            elif typ == 'string':
                self.code.append("read S")
            elif typ == 'bool':
                self.code.append("read B")
            else:
                self.code.append("read I")  # fallback
            self.code.append(f"save {var_name}")

    def visitType(self, ctx):
        if ctx.INT_TYPE():
            return 'int'
        elif ctx.FLOAT_TYPE():
            return 'float'
        elif ctx.BOOL_TYPE():
            return 'bool'
        elif ctx.STRING_TYPE():
            return 'string'
        elif ctx.FILE_TYPE():
            return 'FILE'
        return self.visitChildren(ctx)