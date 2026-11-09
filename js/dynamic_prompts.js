import { app } from "../../scripts/app.js";

// Resolve choices directly: no dependency on core extension registration order.
function resolveDynamicPrompt(text) {
    if (typeof text !== "string") return text;
    let pos = 0;
    function read(inGroup = false) {
        const choices = [""];
        while (pos < text.length) {
            const char = text[pos++];
            if (char === "\\" && pos < text.length && "{}|\\".includes(text[pos])) {
                choices[choices.length - 1] += text[pos++];
            } else if (char === "{") {
                const start = pos - 1;
                const group = read(true);
                choices[choices.length - 1] += group.closed
                    ? group.value : text.slice(start, pos);
            } else if (char === "}" && inGroup) {
                return {closed: true, value: choices[Math.floor(Math.random() * choices.length)]};
            } else if (char === "|" && inGroup) {
                choices.push("");
            } else {
                choices[choices.length - 1] += char;
            }
        }
        return {closed: !inGroup, value: choices.join("|")};
    }
    return read().value;
}

app.registerExtension({
    name: "Magik.TextConcatenate.DynamicPrompts",
    nodeCreated(node) {
        if (node.comfyClass !== "Magik_Text_Concatenate") return;
        for (const widget of node.widgets ?? []) {
            if (!["text1", "text2", "text3"].includes(widget.name)) continue;
            widget.dynamicPrompts = false;
            widget.serializeValue = (workflowNode, widgetIndex) => {
                const toggle = node.widgets?.find(w => w.name === "Enable Dynamic Prompts");
                const value = (toggle?.value ?? true)
                    ? resolveDynamicPrompt(widget.value) : widget.value;
                if (workflowNode?.widgets_values) {
                    workflowNode.widgets_values[widgetIndex] = value;
                }
                return value;
            };
        }
    }
});
