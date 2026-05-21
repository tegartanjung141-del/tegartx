import os
from collections import deque
from PIL import Image, ImageFilter

def perfect_cutout(img_path):
    try:
        img = Image.open(img_path).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        mask = Image.new('L', (width, height), 0)
        mask_pixels = mask.load()
        
        queue = deque()
        visited = set()
        
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
            
            # Determine if pixel is background
            # Either already transparent or a light/white fringe color
            if a < 50 or (r > 180 and g > 180 and b > 180):
                mask_pixels[x, y] = 255
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            
        # Expand the background mask by 2 pixels to completely eat the aliased halo
        dilated_mask = mask.filter(ImageFilter.MaxFilter(5))
        
        # Smooth the edge to avoid pixelated jagged cuts
        smooth_mask = dilated_mask.filter(ImageFilter.GaussianBlur(radius=1.5))
        
        # Apply the inverted mask to the alpha channel
        alpha = Image.eval(smooth_mask, lambda val: 255 - val)
        img.putalpha(alpha)
        
        img.save(img_path, "PNG")
        print(f"Perfected padding and halo for {img_path}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    directory = r"c:\Users\Windows\Desktop\application\public\assets\mascots"
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            perfect_cutout(file_path)
