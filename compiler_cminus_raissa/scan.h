/****************************************************/
/* File: scan.h                                     */
/*                                                  */
/* Autor: Raissa Barbosa dos Santos                 */
/****************************************************/

#ifndef _SCAN_H_
#define _SCAN_H_

// tamanho máximo para um token
#define MAXTOKENLEN 40

// armazena o lexema de cada token
extern char tokenString[MAXTOKENLEN+1];

// retorna o próximo token do arquivo fonte
TokenType getToken(void);

#endif
