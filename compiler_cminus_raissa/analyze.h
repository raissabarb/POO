/****************************************************/
/* File: analyze.h                                  */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#ifndef _ANALYZE_H_
#define _ANALYZE_H_

// constroi a tabela de simbolos pela pré-ordem da árvore sintática
void buildSymtab(TreeNode *);

// faz a verificação de tipos em pós-ordem da árvore sintática
void typeCheck(TreeNode *);

#endif
