def _join_texts(texts, delimiter):
    texts = ["" if text == "undefined" else text for text in texts]

    if delimiter == "\\n":
        delimiter = "\n"

    return delimiter.join(texts)


class MagikText3xConcat:
    """
    Concatenate three text strings with a configurable delimiter.
    Dynamic prompt processing is controlled by the frontend toggle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text2": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text3": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "Enable Dynamic Prompts": ("BOOLEAN", {"default": False}),
                "delimiter": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concat",)
    FUNCTION = "concat_text"

    CATEGORY = "Magik/text"

    def concat_text(self, text1="", text2="", text3="", delimiter="", **kwargs):
        return (_join_texts([text1, text2, text3], delimiter),)


class MagikTextConcat:
    """
    Concatenate two text strings with a configurable delimiter.
    Dynamic prompt processing is controlled by the frontend toggle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text2": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "Enable Dynamic Prompts": ("BOOLEAN", {"default": False}),
                "delimiter": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concat",)
    FUNCTION = "concat_text"

    CATEGORY = "Magik/text"

    def concat_text(self, text1="", text2="", delimiter="", **kwargs):
        return (_join_texts([text1, text2], delimiter),)


NODE_CLASS_MAPPINGS = {
    "Magik_Text_3x_Concat": MagikText3xConcat,
    "Magik_Text_Concat": MagikTextConcat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Magik_Text_3x_Concat": "Magik Text 3x Concat",
    "Magik_Text_Concat": "Magik Text Concat",
}
