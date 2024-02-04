# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

window_title = "MGC run settings"
window_width = 200
window_height = 230


class Settings:
	def __init__(self, root):
		self.root = root
		self.root.title(window_title)
		self.root.geometry(f"{window_width}x{window_height}")

		self.center_window()

		self.runs_entry = self.menu_runs()
		self.map_combobox = self.menu_maps()
		self.reverse_checkbox_var = self.menu_reverse()
		self.exit_checkbox_var = self.menu_exit()
		self.menu_start()

	def center_window(self):
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()

		x = (screen_width // 2) - (window_width // 2)
		y = (screen_height // 2) - (window_height // 2)

		self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

	def menu_runs(self):
		runs_label = ttk.Label(self.root, text="How many runs would you like?")
		runs_label.pack(pady=10)
		runs_entry = ttk.Entry(self.root)
		runs_entry.insert(0, "1")
		runs_entry.pack()

		return runs_entry

	def menu_maps(self):
		import src.maps.maps as maps

		map_label = ttk.Label(self.root, text="Which map would you like?")
		map_label.pack(pady=10)
		map_options = maps.get_maps()
		map_combobox = ttk.Combobox(self.root, values=map_options)
		map_combobox.pack()

		return map_combobox

	def menu_reverse(self):
		reverse_checkbox_var = tk.BooleanVar()
		reverse_checkbox = ttk.Checkbutton(self.root, text="Start run reversed?", variable=reverse_checkbox_var)
		reverse_checkbox.pack(pady=10)

		return reverse_checkbox_var

	def menu_exit(self):
		exit_checkbox_var = tk.BooleanVar()
		exit_checkbox = ttk.Checkbutton(self.root, text="Exit program upon completion?", variable=exit_checkbox_var)
		exit_checkbox.pack()

		return exit_checkbox_var

	def start_run(self):
		import src.state as state
		import src.run.runLogic as glue

		# Save values to state
		state.runs_wanted = int(self.runs_entry.get())
		state.map_selected = self.map_combobox.get()
		state.run_reverse = self.reverse_checkbox_var.get()
		print(state.run_reverse)
		state.exit_on_finish = self.exit_checkbox_var.get()

		# Print values
		# print("Number of Runs:", state.runs_wanted)
		# print("Selected Map:", state.map_selected)
		# print("Exit Program:", state.exit_on_finish)

		# Start run
		glue.begin()

	def menu_start(self):
		start_button = ttk.Button(self.root, text="Start run", command=self.start_run)
		start_button.pack(pady=10)


def run_application():
	# Define the root window.
	root = tk.Tk()
	# Build the main application.
	Settings(root)
	# Run the application.
	root.mainloop()
