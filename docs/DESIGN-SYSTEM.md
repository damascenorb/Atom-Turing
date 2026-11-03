# AtomTuring — Design system

Fonte única: `site/css/site.css` (variáveis em `:root`). Gerado conforme a rotina `/design-system audit` do plugin `design`.

## Auditoria (antes → depois)
| Item | Antes | Depois |
|---|---|---|
| Cores fixas (hex) fora de `:root` | 49 | 6 (neutros usados uma vez) |
| Tamanhos de fonte fixos | 18 | escala com tokens `--t-*` + 5 tamanhos fluidos de título |
| Raios de borda soltos | 7 | tokens `--r-*` |
| Variantes de botão sem uso (`ghost`, `sm`, `white`) | 3 | removidas |
| Estado desativado do botão | ausente | `.pill:disabled` |
| Área de toque dos links do rodapé (celular) | ~20 px | ≥ 44 px |

## Tokens
- **Cores:** `--bg #fff`, `--gray #f5f5f7`, `--ink #1d1d1f`, `--mu #6e6e73` (texto secundário), `--blue #0071e3` (ação), `--link #0066cc`, `--navy #1C2541`, `--slate #3A506B`, `--night #1F2937`, `--line #d2d2d7`, `--err #c0262d`.
- **Tipografia:** fonte do sistema (SF Pro no Mac, Inter nos demais). `--t-xs 12`, `--t-sm 14`, `--t-md 17`, `--t-lg 21`; títulos fluidos com `clamp()`.
- **Raios:** `--r-pill 980`, `--r-card 28`, `--r-card-sm 22`, `--r-field 12`, `--r-chip 10`.
- **Espaço:** `--s-1 8` … `--s-6 48`.
- **Movimento:** `--ease cubic-bezier(.23,1,.32,1)`; tudo respeita `prefers-reduced-motion`.

## Componentes
| Componente | Variantes | Estados |
|---|---|---|
| `.pill` (botão) | padrão azul; `.pill--nav` (menu) | hover, active (0.96), disabled, focus |
| `.lk` (link com seta) | claro/escuro (`.on-dark`) | hover, focus |
| `.tile` (tela de destaque) | `--dark`, `--navy`, `--slate`, `--night`, `--blue`, `--hero`, `--plain` | hover (zoom da foto) |
| `.card` (galeria) | — | hover (zoom) |
| `.rail` + `.rail-btn` | — | disabled nas pontas |
| `.f` (campo), `.opts` (opções) | texto, select, textarea, chips | focus, checked, invalid |
| `.faq` | — | aberto/fechado |

## Regras
1. Cor nova entra como token antes de ser usada.
2. Botão preenchido só em azul (`--blue`); em fundo escuro use link branco.
3. Foto de tela com foco definido (`object-position`) e proporção fixa em pares (4:3).
4. Toda imagem tem `alt`, `width` e `height`.
