def _evaluate(python_expression, state):

    exec(python_expression, state)
    print("output state", state)

    return state


class PythonAnyToAny:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "python_expression": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "float1": ("FLOAT", {}),
                "float2": ("FLOAT", {}),
                "float3": ("FLOAT", {}),
                "float4": ("FLOAT", {}),
                "int1": ("INT", {}),
                "int2": ("INT", {}),
                "int3": ("INT", {}),
                "int4": ("INT", {}),
                "str1": ("STRING", {}),
                "str2": ("STRING", {}),
                "str3": ("STRING", {}),
                "str4": ("STRING", {}),
            },
        }

    RETURN_NAMES = (
        "float1",
        "float2",
        "float3",
        "float4",
        "int1",
        "int2",
        "int3",
        "int4",
        "str1",
        "str2",
        "str3",
        "str4",
    )
    RETURN_TYPES = (
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "FLOAT",
        "INT",
        "INT",
        "INT",
        "INT",
        "STRING",
        "STRING",
        "STRING",
        "STRING",
    )
    FUNCTION = "process"
    CATEGORY = "Utility"

    def process(
        self,
        python_expression,
        float1,
        float2,
        float3,
        float4,
        int1,
        int2,
        int3,
        int4,
        str1,
        str2,
        str3,
        str4,
    ):

        state = {k: v for k, v in locals().items() if k not in ["self"]}

        _evaluate(python_expression, state)

        print(f"PythonAnyToAny(): locals: {locals()}")

        output = (
            state["float1"],
            state["float2"],
            state["float3"],
            state["float4"],
            state["int1"],
            state["int2"],
            state["int3"],
            state["int4"],
            state["str1"],
            state["str2"],
            state["str3"],
            state["str4"],
        )

        print(f"PythonAnyToAny(): output: {output}")

        return output


class SplitAndSelectByIndex:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_string": ("STRING", {"default": "", "multiline": False}),
                "split_by_string": ("STRING", {"default": "", "multiline": False}),
                "index_to_output": ("INT", {"default": "0", "min": 0, "max": 99999}),
            }
        }

    RETURN_TYPES = ("FLOAT", "INTEGER", "STRING")
    FUNCTION = "process"
    CATEGORY = "Utility"

    def process(self, input_string, split_by_string, index_to_output):
        print(f'SplitAndSelectByIndex.process() input string = "{input_string}"')
        print(f'SplitAndSelectByIndex.process() split by string = "{split_by_string}"')
        print(f"SplitAndSelectByIndex.process() index = {index_to_output}")
        parts = input_string.split(split_by_string)
        print(f"SplitAndSelectByIndex.process() parts = {parts}")

        string_val = parts[index_to_output] if index_to_output < len(parts) else None

        float_val = None
        try:
            float_val = float(string_val)
        except:
            pass

        int_val = None
        try:
            int_val = int(string_val)
        except:
            pass

        return (float_val, int_val, string_val)


NODE_CLASS_MAPPINGS = {
    "PythonAnyToAny": PythonAnyToAny,
    "SplitAndSelectByIndex": SplitAndSelectByIndex,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PythonAnyToAny": "Python - Any To Any",
    "SplitAndSelectByIndex": "Split String and Select by Index",
}
