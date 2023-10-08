import ddddocr
ocr = ddddocr.DdddOcr(det=False, ocr=False,
                      import_onnx_path="ruoyi.onnx", charsets_path="charsets.json")
with open('1.png', 'rb') as f:
    image_bytes = f.read()
formula = ocr.classification(image_bytes)
code = eval(formula.replace('=？', '').replace('÷', '/').replace('×', '*'))
