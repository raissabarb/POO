/****************************************************/
/* File: util.h                                     */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#ifndef _UTIL_H_
#define _UTIL_H_

// imprime token e seu lexema
void printToken( TokenType, const char* );

// cria um nó de uma declaração para a construção da árvore sintática
TreeNode * newStmtNode(StatementKind);

// cria um nó de uma expressão para a construção da árvore sintática
TreeNode * newExpNode(ExpressionIdentifier);

// aloca e faz uma cópia da string existente
char * copyString( char * );

// imprime a árvore sintática 
void printTree( TreeNode * );

#endif
