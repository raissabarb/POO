/****************************************************/
/* File: main.c                                     */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#include "globals.h"

// caso só tenha o scanner, NO_PARSE = true
#define NO_PARSE FALSE

// caso só tenha o parser, NO_ANALYZE = true
#define NO_ANALYZE FALSE

// caso o compilador não gere um código, NO_CODE = true 
#define NO_CODE TRUE

#include "util.h"
// se só tiver o scanner, adiciona o scan.h
#if NO_PARSE 
#include "scan.h"
#else
#include "parse.h"
#if !NO_ANALYZE
#include "analyze.h"
#if !NO_CODE

#endif
#endif
#endif

// variáveis globais
int lineno = 0;
FILE *source;
FILE *listing;
FILE *code;

// aloca e define as tracing files
int EchoSource = FALSE;
int TraceScan = TRUE;
int TraceParse = TRUE;
int TraceAnalyze = TRUE;
int TraceCode = FALSE;

int Error = FALSE;

int main(int argc, char *argv[]){

  TreeNode *syntaxTree;
  char pgm[120];   // nome do código que será analisado

  if (argc != 2){
    fprintf(stderr, "usage: %s <filename>\n", argv[0]);
    exit(1);
  }

  strcpy(pgm, argv[1]);

  // arquivo podendo virar cms
  if (strchr(pgm, '.') == NULL)
    strcat(pgm, ".cms");
  source = fopen(pgm, "r");

  if (source == NULL){
    fprintf(stderr, "O arquivo %s não foi encontrado.\n", pgm);
    exit(1);
  }

  // colocando mensagem de início de compilação na tela
  listing = stdout; 
  fprintf(listing, "\nIniciando a compilação de %s ...\n\n", pgm);
#if NO_PARSE
  while (getToken() != ENDFILE)
    ;
#else
  syntaxTree = parse();
  if (TraceParse){
    fprintf(listing, "\n\n>>> Árvore sintática <<<\n\n");
    printTree(syntaxTree);
  }
#if !NO_ANALYZE
  if (!Error)
  {
    if (TraceAnalyze)
      fprintf(listing, "\nCriando tabela de símbolos...\n");
    buildSymtab(syntaxTree);
    if (TraceAnalyze)
      fprintf(listing, "\nVerificando tipos...\n");
    typeCheck(syntaxTree);
  }
#if !NO_CODE
  if (!Error){
    char *codefile;
    int fnlen = strcspn(pgm, ".");
    codefile = (char *)calloc(fnlen + 4, sizeof(char));
    strncpy(codefile, pgm, fnlen);
    strcat(codefile, ".tm");
    code = fopen(codefile, "w");
    if (code == NULL){
      printf("Não foi possível abrir o arquivo %s\n", codefile);
      exit(1);
    }
    codeGen(syntaxTree, codefile);
    fclose(code);
  }
#endif
#endif
#endif

  fclose(source);
  return 0;
}
