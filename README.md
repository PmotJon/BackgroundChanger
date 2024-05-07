# Background Changer using Remove.bg API

This Python script allows you to automatically remove the background from an image using the Remove.bg API. You can integrate this feature into your applications or workflows. Here are some key points about the code:

1. **Function `bg_changer`**:
    - This function takes two parameters: `img` (path to the image) and `bg_color` (background color code).
    - It uses the Remove.bg API to remove the image background.
    - The resulting image without a background is saved with a filename reflecting the current timestamp.

2. **Usage**:
    - You can run this script by providing the image path and the background color code as arguments.
    - Example usage:
        ```
        python.exe .\main.py .\images\my_image.jpg
        ```
        or
        ```
        python.exe .\main.py images/profile-1.jpg
        ```

3. **Input Background Color**:
    - You can input the color code in hexadecimal format (e.g., `#1D76DB` for blue, `#DB231D` for red, or `#FFFF00` for yellow).

4. **Output**:
    - The resulting image without a background will be saved in the "output" folder with a filename reflecting the current timestamp.
