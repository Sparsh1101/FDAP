import rasterio
import os

# Open the input TIF file


def print():
    k = 1
    for z in range(1, 26):
        with rasterio.open("./ALL_FLOOD/" + str(z) + '_P.tif') as src:

            # Get the size of the input image
            width, height = src.width, src.height

            # Compute the number of 256x256 pixel images needed in the x and y directions
            num_x = width // 256
            num_y = height // 256

            # Loop over each 256x256 pixel image
            for i in range(num_x):
                for j in range(num_y):

                    # Compute the window to read from the input TIF file
                    window = rasterio.windows.Window(
                        i * 256, j * 256, 256, 256)

                    # Read the data for this window from the input TIF file
                    data = src.read(window=window)

                    # Create a new TIF file for this 256x256 pixel image
                    output_file = str(k) + "_P_256.tif"
                    with rasterio.open("./ALL_FLOOD_256/" + output_file, 'w', driver='GTiff', width=256, height=256, count=src.count, dtype=src.dtypes[0], crs=src.crs, transform=src.window_transform(window)) as dst:

                        # Write the data to the output TIF file
                        dst.write(data)
                    k += 1


    # Output a list of the output file names
    # output_files = [f"output_{i}_{j}.tif" for i in range(num_x) for j in range(num_y)]
    # print(f"Output files: {output_files}")
print()
