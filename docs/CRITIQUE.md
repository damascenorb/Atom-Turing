# AtomTuring — Crítica de design

Seguindo a rotina `/design-critique` do plugin `design`. Contexto: site de serviços (manutenção de computadores e redes), público: pessoas e empresas; fase: refinamento.

## Impressão geral
Direção clara e profissional: telas grandes, foto de pessoa trabalhando e título curto. A maior oportunidade era a conversão: o contato principal estava escondido.

## Usabilidade
| Achado | Gravidade | Ação | Status |
|---|---|---|---|
| Contato no menu era um link de 12 px, quase invisível | 🔴 | virou botão azul "WhatsApp" | feito |
| Cada tela tem dois links iguais ("Saiba mais" e "Pedir orçamento") | 🟡 | manter: um explica, outro converte | mantido |
| Páginas internas sem rota óbvia para o orçamento além do menu | 🟡 | botão do menu agora fixo em todas as páginas | feito |

## Hierarquia
- Primeiro olhar: foto do técnico + título "Computadores e componentes". Correto.
- Fluxo: título → frase → links → foto. Consistente em todas as telas.
- Ênfase: links de 21 px bem legíveis; texto de apoio em cinza com contraste 4,66:1.

## Consistência
| Elemento | Problema | Ação | Status |
|---|---|---|---|
| Cores, fontes e raios | valores soltos no CSS | tokens (ver DESIGN-SYSTEM.md) | feito |
| Variantes de botão | 3 sem uso | removidas | feito |

## Acessibilidade
- Contraste: texto principal e links passam de 4,5:1.
- Toque: rodapé no celular abaixo de 44 px → corrigido.
- Texto alternativo: todas as imagens têm `alt`.
- Movimento: respeita a preferência do sistema.

## O que funciona bem
- Fotos reais com enquadramento definido.
- Estrutura repetível (tela, par, galeria) fácil de manter.
- Formulários simples, com resposta por WhatsApp ou e-mail.

## Prioridades abertas
1. **Prova social:** adicionada a seção "Por que a AtomTuring" com fatos verificáveis (CNPJ, orçamento sem compromisso, suporte) e link do Instagram. Depoimentos de clientes não foram inventados.
2. **Foto de Wi-Fi** (letreiro) é a mais fraca; trocar por foto de roteador/ponto de acesso.
3. **Fotos próprias** da AtomTuring no lugar das de banco de imagens.
