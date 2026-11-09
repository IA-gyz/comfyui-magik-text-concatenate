class MagikTextConcatenate:
    """
    Concatenate up to three text strings with a configurable delimiter.
    Dynamic prompt processing is controlled by the frontend toggle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text2": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "text3": ("STRING", {"multiline": True, "default": "", "dynamicPrompts": False}),
                "Enable Dynamic Prompts": ("BOOLEAN", {"default": True}),
                "delimiter": ("STRING", {"default": ",", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concat",)
    FUNCTION = "concat_text"

    CATEGORY = "Magik/text"

    def concat_text(self, text1="", text2="", text3="", delimiter=",", **kwargs):
        text1 = "" if text1 == "undefined" else text1
        text2 = "" if text2 == "undefined" else text2
        text3 = "" if text3 == "undefined" else text3

        if delimiter == "\\n":
            delimiter = "\n"

        concat = delimiter.join([text1, text2, text3])

        return (concat,)


NODE_CLASS_MAPPINGS = {
    "Magik_Text_Concatenate": MagikTextConcatenate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Magik_Text_Concatenate": "Magik Text Concatenate",
}
