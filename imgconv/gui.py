
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path
from imgconv.comon_img import convert_image, ImageFormat  # Import the core conversion function and ImageFormat enum

class ImageConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter (HEIF / AVIF)")
        self.geometry("500x300")
        self.resizable(True, True)

        # Input folder
        self.input_path_var = tk.StringVar()
        self.output_path_var = tk.StringVar()
        self.format_var = tk.StringVar(value=ImageFormat.HEIF.value)

        ttk.Label(self, text="Input Folder:").pack(anchor='w', padx=10, pady=(15, 0))
        ttk.Entry(self, textvariable=self.input_path_var, width=60).pack(padx=10)
        ttk.Button(self, text="Browse", command=self.browse_input).pack(pady=5)

        ttk.Label(self, text="Output Folder:").pack(anchor='w', padx=10)
        ttk.Entry(self, textvariable=self.output_path_var, width=60).pack(padx=10)
        ttk.Button(self, text="Browse", command=self.browse_output).pack(pady=5)

        ttk.Label(self, text="Format:").pack(anchor='w', padx=10)
        ttk.Combobox(self, textvariable=self.format_var, values=[f.value for f in ImageFormat]).pack(padx=10, pady=5)
        ttk.Button(self, text="Convert", command=self.run_conversion).pack(pady=10)


    def browse_input(self):
        path = filedialog.askdirectory(title="Select Input Directory")
        if path:
            self.input_path_var.set(path)

    def browse_output(self):
        path = filedialog.askdirectory(title="Select Output Directory")
        if path:
            self.output_path_var.set(path)

    def run_conversion(self):
        input_path = Path(self.input_path_var.get())
        output_path = Path(self.output_path_var.get())
        format_str = self.format_var.get()

        if not input_path.exists() or not output_path.exists():
            messagebox.showerror("Error", "Both input and output directories must exist.")
            return

        try:
            convert_image(input_path, output_path, ImageFormat(format_str))
            messagebox.showinfo("Success", f"Images converted to {format_str.upper()} successfully.")
            # self.quit()
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

def gui_main():
    app = ImageConverterGUI()
    app.mainloop()


if __name__ == "__main__":
    gui_main()