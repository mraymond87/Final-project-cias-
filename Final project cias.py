#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:40:26 2024

@author: raymondm
"""

import tkinter as tk
from tkinter import messagebox

class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Manager")
        
        self.recipes = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to Recipe Manager!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Recipes", command=self.view_recipes)
        self.view_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def add_recipe(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Recipe")

        tk.Label(add_window, text="Recipe Title:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(add_window)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Ingredients (separated by commas):").grid(row=1, column=0, padx=5, pady=5)
        self.ing_entry = tk.Entry(add_window)
        self.ing_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Instructions:").grid(row=2, column=0, padx=5, pady=5)
        self.inst_entry = tk.Entry(add_window)
        self.inst_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(add_window, text="Save Recipe", command=self.save_recipe).grid(row=3, columnspan=2, pady=10)

    def save_recipe(self):
        title = self.title_entry.get()
        ingredients = self.ing_entry.get().split(",")
        instructions = self.inst_entry.get()

        if not title or not ingredients or not instructions:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        new_recipe = Recipe(title, ingredients, instructions)
        self.recipes.append(new_recipe)
        messagebox.showinfo("Success", "Recipe added successfully!")
        self.title_entry.delete(0, tk.END)
        self.ing_entry.delete(0, tk.END)
        self.inst_entry.delete(0, tk.END)

    def view_recipes(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Recipes")

        if not self.recipes:
            messagebox.showinfo("No recipes", "No recipes available.")
            return

        for i, recipe in enumerate(self.recipes, start=1):
            recipe_text = f"Recipe {i}:\nTitle: {recipe.title}\nIngredients: {', '.join(recipe.ingredients)}\nInstructions: {recipe.instructions}\n\n"
            tk.Label(view_window, text=recipe_text, justify="left").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
