class Interpreter:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.pc = 0
        self.instructions = []
        
    def load_program(self, filename):
        """Load a program from a file"""
        with open(filename, 'r', encoding='utf-8') as f:
            self.instructions = []
            # First pass: collect all instructions and find labels
            line_num = 0
            for line in f:
                line = line.strip()
                if not line or line.startswith('//'):
                    continue
                
                parts = line.split(None, 1)
                if parts[0] == 'label':
                    label_num = int(parts[1])
                    self.labels[label_num] = line_num
                else:
                    self.instructions.append(line)
                    line_num += 1
    
    def run(self):
        """Run the loaded program"""
        self.pc = 0
        while self.pc < len(self.instructions):
            self.execute(self.instructions[self.pc])
            self.pc += 1
    
    def execute(self, instruction):
        """Execute a single instruction"""
        parts = instruction.split()
        opcode = parts[0]
        
        if opcode == 'push':
            type_code = parts[1]
            if type_code == 'I':
                self.stack.append(int(parts[2]))
            elif type_code == 'F':
                self.stack.append(float(parts[2]))
            elif type_code == 'B':
                self.stack.append(parts[2].lower() == 'true')
            elif type_code == 'S':
                # Handle string literals with spaces and escape quotes
                value = " ".join(parts[2:])
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                self.stack.append(value)
            else:
                raise ValueError(f"Unknown type code: {type_code}")
        
        elif opcode == 'pop':
            self.stack.pop()
            
        elif opcode == 'save':
            var_name = parts[1]
            self.memory[var_name] = self.stack[-1]
            
        elif opcode == 'load':
            var_name = parts[1]
            if var_name not in self.memory:
                raise ValueError(f"Variable {var_name} not defined")
            self.stack.append(self.memory[var_name])
            
        elif opcode == 'print':
            count = int(parts[1])
            values = [str(self.stack[-i]) for i in range(count, 0, -1)]
            print("".join(values))
            
        elif opcode == 'add':
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            if type_code == 'I':
                self.stack.append(a + b)
            else:
                raise ValueError(f"Unsupported add type: {type_code}")
                
        elif opcode == 'sub':
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a - b)
            
        elif opcode == 'mul':
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a * b)
            
        elif opcode == 'div':
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a / b)
            
        elif opcode == 'lt':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a < b)
            
        elif opcode == 'gt':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a > b)
            
        elif opcode == 'eq':
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a == b)
            
        elif opcode == 'fjmp':
            label = int(parts[1])
            condition = self.stack.pop()
            if not condition:
                self.pc = self.labels[label] - 1  # -1 because pc will be incremented
                
        elif opcode == 'jmp':
            label = int(parts[1])
            self.pc = self.labels[label] - 1  # -1 because pc will be incremented
            
        elif opcode == 'read':
            type_code = parts[1]
            if type_code == 'I':
                value = int(input("Enter an integer: "))
            elif type_code == 'F':
                value = float(input("Enter a float: "))
            elif type_code == 'B':
                value = input("Enter a boolean (true/false): ").lower() == 'true'
            elif type_code == 'S':
                value = input("Enter a string: ")
            else:
                raise ValueError(f"Unknown type code for read: {type_code}")
            self.stack.append(value)
        
        elif opcode == 'itof':
            # Convert integer to float
            value = self.stack.pop()
            if isinstance(value, int):
                self.stack.append(float(value))
            else:
                raise ValueError(f"Expected int for itof operation, got {type(value)}")
        
        elif opcode == 'not':
            # Logical NOT
            value = self.stack.pop()
            self.stack.append(not value)
        
        elif opcode == 'and':
            # Logical AND
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a and b)
        
        elif opcode == 'or':
            # Logical OR
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a or b)
        
        elif opcode == 'mod':
            # Modulo operation
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a % b)
        
        elif opcode == 'concat':
            # String concatenation
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(str(a) + str(b))
        
        elif opcode == 'uminus':
            # Unary minus
            type_code = parts[1]
            value = self.stack.pop()
            self.stack.append(-value)
        
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)
        
    interpreter = Interpreter()
    interpreter.load_program(sys.argv[1])
    interpreter.run()