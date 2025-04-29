push S "<Relational operators>"
push S "1<5: "
push I 1
push I 5
lt I
push S "1>3.5: "
push I 1
push F 3.5
gt I
push S "aa==aa: "
push S "aa"
push S "aa"
eq I
push S "aa==ab: "
push S "aa"
push S "ab"
eq I
push S "aa!=ab: "
push S "aa"
push S "ab"
eq I
push S ""
push S "<Logic operators>"
push S "false and true (false):"
push B false
push B true
and
push S "false or true (true):"
push B false
push B true
or
push S "not 1==2 (true):"
push I 1
push I 2
eq I
not
push S "true or false and true (true):"
push B true
push B false
or
push B true
and
