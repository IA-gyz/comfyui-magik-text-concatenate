# Magik Text Concatenate

Extract this folder into ComfyUI/custom_nodes/, restart ComfyUI, then refresh the browser.
Find the nodes under **Magik/text**.

Three text concat nodes, all with one STRING output (`concat`). Inputs can also receive connected strings using ComfyUI widget-to-input conversion.

- **Magik Text Concat**: two multiline STRING inputs.
- **Magik Text 3x Concat**: three multiline STRING inputs.
- **Magik Text 9x Concat**: nine multiline STRING inputs, delimiter default is a comma.

Shared behaviour:

- `delimiter`: inserted between all inputs. Enter literal `\n` for line breaks.
- Empty inputs retain their position: they still contribute delimiters.
- `Enable Dynamic Prompts`: resolves choices such as `{red|blue}` in text widgets when queued. Supports nested choices and escaped braces/pipes. Connected strings pass through as supplied. Default is on for the 9x node, off for the others.

No extra dependencies.

### Merged pack

`Magik Text 9x Concat` was previously published in its own repo, [comfyui-magik-text-9x-concat](https://github.com/IA-gyz/comfyui-magik-text-9x-concat), which is now deprecated. If both packs are installed, remove the old one; the node keeps its ID (`Magik_Text_9x_Concat`) and widgets, so existing workflows load unchanged.
