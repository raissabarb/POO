/****************************************************/
/* File: util.c                                     */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#include "globals.h"
#include "util.h"

void printToken(TokenType token, const char *tokenString){
  switch (token){
    case IF: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case ELSE: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case INT: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case RETURN: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case VOID: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case WHILE: fprintf(listing, "Palavra reservada: %s\n", tokenString); break;
    case ATRIBUI: fprintf(listing, "Simbolo: =\n"); break;
    case MENOR: fprintf(listing, "Simbolo: <\n"); break;
    case IGUAL: fprintf(listing, "Simbolo: ==\n"); break;
    case MAIOR: fprintf(listing, "Simbolo: >\n"); break;
    case MENORIG: fprintf(listing, "Simbolo: <=\n"); break;
    case MAIORIG: fprintf(listing, "Simbolo: >=\n"); break;
    case DIFERENTE: fprintf(listing, "Simbolo: !=\n"); break;
    case LCOLCHETE: fprintf(listing, "Simbolo: [\n"); break;
    case RCOLCHETE: fprintf(listing, "Simbolo: ]\n"); break;
    case LCHAVE: fprintf(listing, "Simbolo: {\n"); break;
    case RCHAVE: fprintf(listing, "Simbolo: }\n"); break;
    case LPARENT: fprintf(listing, "Simbolo: (\n"); break;
    case RPARENT: fprintf(listing, "Simbolo: )\n"); break;
    case PTOVIRG: fprintf(listing, "Simbolo: ;\n"); break;
    case VIRGULA: fprintf(listing, "Simbolo: ,\n"); break;
    case MAIS: fprintf(listing, "Simbolo: +\n"); break;
    case MENOS: fprintf(listing, "Simbolo: -\n"); break;
    case MULT: fprintf(listing, "Simbolo: *\n"); break;
    case BARRA: fprintf(listing, "Simbolo: /\n"); break;
    case ENDFILE: fprintf(listing, "EOF\n"); break;
    case NUM: fprintf(listing, "Número: %s\n", tokenString); break;
    case ID: fprintf(listing, "ID: %s\n", tokenString); break;
    case ERROR: fprintf(listing, "ERROR: %s\n", tokenString); break;
    default:
      fprintf(listing, "Token desconhecido: %d\n", token);
  }
}

void printTokenForError(TokenType token, const char *tokenString){
  switch (token){
    case IF: fprintf(listing, "%s", tokenString); break;
    case ELSE: fprintf(listing, "%s", tokenString); break;
    case INT: fprintf(listing, "%s", tokenString); break;
    case RETURN: fprintf(listing, "%s", tokenString); break;
    case VOID: fprintf(listing, "%s", tokenString); break;
    case WHILE: fprintf(listing, "%s", tokenString); break;
    case ATRIBUI: fprintf(listing, "="); break;
    case MENOR: fprintf(listing, "<"); break;
    case IGUAL: fprintf(listing, "=="); break;
    case MAIOR: fprintf(listing, ">"); break;
    case MENORIG: fprintf(listing, "<="); break;
    case MAIORIG: fprintf(listing, ">="); break;
    case DIFERENTE: fprintf(listing, "!="); break;
    case LCOLCHETE: fprintf(listing, "["); break;
    case RCOLCHETE: fprintf(listing, "]"); break;
    case LCHAVE: fprintf(listing, "{"); break;
    case RCHAVE: fprintf(listing, "}"); break;
    case LPARENT: fprintf(listing, "("); break;
    case RPARENT: fprintf(listing, ")"); break;
    case PTOVIRG: fprintf(listing, ";"); break;
    case VIRGULA: fprintf(listing, ","); break;
    case MAIS: fprintf(listing, "+"); break;
    case MENOS: fprintf(listing, "-"); break;
    case MULT: fprintf(listing, "*"); break;
    case BARRA: fprintf(listing, "/"); break;
    case ENDFILE: fprintf(listing, "EOF"); break;
    case NUM: fprintf(listing, "%s", tokenString); break;
    case ID: fprintf(listing, "%s", tokenString); break;
    case ERROR: fprintf(listing, "%s", tokenString); break;
    default:
      fprintf(listing, "%d", token);
  }
}

void aggScope(TreeNode *t, char *scope){
  int i;
  while (t != NULL){
    for (i = 0; i < MAXCHILDREN; ++i){
      t->attr.scope = scope;
      aggScope(t->child[i], scope);
    }
    t = t->sibling;
  }
}

TreeNode *newStmtNode(StatementKind kind){
  TreeNode *t = (TreeNode *)malloc(sizeof(TreeNode));
  int i;
  if (t == NULL)
    fprintf(listing, "Out of memory error na linha %d\n", lineno);
  else{
    for (i = 0; i < MAXCHILDREN; i++)
      t->child[i] = NULL;
    t->sibling = NULL;
    t->nodekind = statementK;
    t->kind.stmt = kind;
    t->lineno = lineno;
    t->attr.scope = "global";
  }
  return t;
}

TreeNode *newExpNode(ExpressionIdentifier kind){
  TreeNode *t = (TreeNode *)malloc(sizeof(TreeNode));
  int i;
  if (t == NULL)
    fprintf(listing, "Out of memory error na linha %d\n", lineno);
  else{
    for (i = 0; i < MAXCHILDREN; i++)
      t->child[i] = NULL;
    t->sibling = NULL;
    t->nodekind = expressionK;
    t->kind.exp = kind;
    t->lineno = lineno;
    t->type = VOID;
    t->attr.scope = "global";
  }
  return t;
}

char *copyString(char *s){
  int n;
  char *t;
  if (s == NULL)
    return NULL;
  n = strlen(s) + 1;
  t = malloc(n);
  if (t == NULL)
    fprintf(listing, "Out of memory error na linha %d\n", lineno);
  else
    strcpy(t, s);
  return t;
}

static int indentno = 0; 

#define INDENT indentno += 2
#define UNINDENT indentno -= 2

static void printSpaces(void){
  int i;
  for (i = 0; i < indentno; i++)
    fprintf(listing, " ");
}

void printTree(TreeNode *tree){
  int i;
  INDENT;
  while (tree != NULL){
    printSpaces();
    if (tree->nodekind == statementK){
      switch (tree->kind.stmt){
        case ifK:
          fprintf(listing, "If\n");
          break;
        case assignK:
          fprintf(listing, "Atribuição\n");
          break;
        case whileK:
          fprintf(listing, "While\n");
          break;
        case variableK:
          fprintf(listing, "Variável %s\n", tree->attr.name);
          break;
        case functionK:
          fprintf(listing, "Função %s\n", tree->attr.name);
          break;
        case callK:
          fprintf(listing, "Chamada para função %s \n", tree->attr.name);
          break;
        case returnK:
          fprintf(listing, "Return\n");
          break;

        default:
          fprintf(listing, "Tipo de ExpNode desconhecido\n");
          break;
      }
    }
    else if (tree->nodekind == expressionK){
      switch (tree->kind.exp){
        case operationK:
          fprintf(listing, "Operações: ");
          printToken(tree->attr.op, "\0");
          break;
        case constantK:
          fprintf(listing, "Constante: %d\n", tree->attr.val);
          break;
        case idK:
          fprintf(listing, "Id: %s\n", tree->attr.name);
          break;
        case vectorK:
          fprintf(listing, "Vetor: %s\n", tree->attr.name);
          break;
        case vectorIdK:
          fprintf(listing, "Index [%d]\n", tree->attr.val);
          break;
        case typeK:
          fprintf(listing, "Tipo %s\n", tree->attr.name);
          break;

        default:
          fprintf(listing, "Tipo de ExpNode desconhecido\n");
          break;
      }
    }
    else
      fprintf(listing, "Tipo de nó desconhecido\n");
    for (i = 0; i < MAXCHILDREN; i++)
      printTree(tree->child[i]);
    tree = tree->sibling;
  }
  UNINDENT;
}



