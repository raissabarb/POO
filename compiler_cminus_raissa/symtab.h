/****************************************************/
/* File: symtab.h                                   */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#ifndef _SYMTAB_H_
#define _SYMTAB_H_

// insere número de linhas e locação de memória na tabela de simbolos (loc é inserido somente uma vez, na primeira ocorrencia)
void stInsert(char * name, int lineno, int loc, char* scope, char* typeID, char* typeData);

// retorna a locação de memória de uma variável ou -1 caso ela não seja encontrada
int st_lookup (char * name, char* scope );

char* statementFinderType(char* name, char* scope);

// imprime a tabela de simbolos formatada
void printSymTab(FILE * listing);

#endif
