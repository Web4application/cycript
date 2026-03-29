%{
  open Ast
%}

%token <string> ID
%token ASYNC AWAIT SELECTOR LBRACK RBRACK EOF
%start <Ast.expr> main

%%

main:

  | e = expr EOF { e }

expr:
  | ID { Var $1 }
  | LBRACK obj=expr msg=expr RBRACK { ObjCMessage(obj, msg) }
  | AWAIT e=expr { AwaitExpr(e) }
