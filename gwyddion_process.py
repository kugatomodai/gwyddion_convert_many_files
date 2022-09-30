import os, sys, re
import gwy

print("\nPlease enter the files' folrder directory:")
print("(Example: 'C:\Users\username\Desktop\dataset')")
directory = str(raw_input())
# Change the current folder's directory and get the name
os.chdir(directory)
location = os.getcwd()

# Make a list from the filenames in the folder in alphanumerical order
all_files = sorted_alphanumeric(os.listdir(location))

# Create a list for only the files gwyddion can open
files = []

# Load all files from the folder and fill the lists we created
for i in range(len(all_files)) :
	
	try :
		# Load the files of the folder and add them to the data browser
		container = gwy.gwy_file_load(all_files[i], gwy.RUN_NONINTERACTIVE)
		gwy.gwy_app_data_browser_add(container)
	

        ###ここに画像の変換->指定ディレクトリに保存のスクリプト
        filename = container.get_string_by_name("/filename")
        filebase = filename[0:-4]

        ###画像の変換
        ###
        ###

        # save fixed file
        gwy.utils.save_dield_to_png(container, "/0/data", filebase+"_fixed.png", gwy.RUN_INTERACTIVE)
        gwy.gwy_file_save(container, filebase)


        # Remove the file (container) from the data browser to avoid overloading the memory
		gwy.gwy_app_data_browser_remove(container)

    except Exception:
		sys.exc_clear()
