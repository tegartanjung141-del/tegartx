import os
from collections import deque
from PIL import Image

def remove_bg_floodfill(img_path):
    try:
        img = Image.open(img_path).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        queue = deque()
        visited = set()
        
        # Add all border pixels
        for i in range(width):
            queue.append((i, 0))
            queue.append((i, height-1))
            visited.add((i, 0))
            visited.add((i, height-1))
        for i in range(1, height-1):
            queue.append((0, i))
            queue.append((width-1, i))
            visited.add((0, i))
            visited.add((width-1, i))
            
        while queue:
            x, y = queue.popleft()
            r, g, b, a = pixels[x, y]
            
            # If the pixel is white-ish (background)
            if r > 240 and g > 240 and b > 240 and a > 0:
                pixels[x, y] = (255, 255, 255, 0)
                
                # Check neighbors
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            
        img.save(img_path, "PNG")
        print(f"Successfully removed background from {img_path}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    directory = r"c:\Users\Windows\Desktop\application\public\assets\mascots"
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            remove_bg_floodfill(file_path)
