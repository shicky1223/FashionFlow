"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export default function WardrobeUploader() {
  const [file, setFile] = useState<File | null>(null)
  const [description, setDescription] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return

    const formData = new FormData()
    formData.append("image", file)
    formData.append("description", description)

    try {
      const response = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      })
      if (response.ok) {
        console.log("Image uploaded successfully")
        setFile(null)
        setDescription("")
      } else {
        console.error("Failed to upload image")
      }
    } catch (error) {
      console.error("Error uploading image:", error)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <h2 className="text-2xl font-semibold">Add to Your Wardrobe</h2>
      <div>
        <Label htmlFor="image">Upload Image</Label>
        <Input
          id="image"
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          required
        />
      </div>
      <div>
        <Label htmlFor="description">Description</Label>
        <Input
          id="description"
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="E.g., Blue denim jeans, casual wear"
          required
        />
      </div>
      <Button type="submit">Upload Item</Button>
    </form>
  )
}

