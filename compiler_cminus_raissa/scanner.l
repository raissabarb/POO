
%{

#include "globals.h"
#include "util.h"
#include "scan.h"

char tokenString[MAXTOKENLEN+1];
static int yylex(void);

%}

digito [0-9]
numero {digito}+
letra [a-zA-Z]
identificador {letra}+
linhaNova \n
espacoBranco [ \t]+

%%

"/*"               { char c;
                     do{ 
                      c = input();
                      if (c == EOF) break;
                      if (c == '\n') lineno++;
                        if (c == '*'){ 
                          if(input() == '/')
                          break;
                        }		
                    } while (1);
                   }
"if"               {return IF;}
"else"             {return ELSE;}
"int"              {return INT;}
"return"           {return RETURN;}
"void"             {return VOID;}
"while"            {return WHILE;}
"+"                {return MAIS;}
"-"                {return MENOS;}
"*"                {return MULT;}
"/"                {return BARRA;}
"<"                {return MENOR;}
"<="               {return MENORIG;}
">"                {return MAIOR;}
">="               {return MAIORIG;}
"=="               {return IGUAL;}
"="                {return ATRIBUI;}
"!="               {return DIFERENTE;}
","                {return VIRGULA;}
";"                {return PTOVIRG;}
"("                {return LPARENT;}
")"                {return RPARENT;}
"["                {return LCOLCHETE;}
"]"                {return RCOLCHETE;}
"{"                {return LCHAVE;}
"}"                {return RCHAVE;}
{numero}           {return NUM;}
{identificador}    {return ID;}
{linhaNova}        {lineno++;}
{espacoBranco}     {         }
.                  {return ERROR;}

%%

TokenType getToken(void){

  static int firstTime = TRUE;
  TokenType currentToken;

  if (firstTime){ 
    firstTime = FALSE;
    lineno++;
    yyin = source;
    yyout = listing;
  }
  currentToken = yylex();

  strncpy(tokenString,yytext,MAXTOKENLEN);

  if (TraceScan) {
    fprintf(listing,"\t%d: ",lineno);
    printToken(currentToken,tokenString);
  }

  if(currentToken == ERROR){
    printf("\nErro Léxico: ");
    printTokenForError(currentToken,tokenString);
    printf(" Linha: %d\n", lineno);
    Error = TRUE;
  }

  return currentToken;
}
