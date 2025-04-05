import WardrobeUploader from "@/components/wardrobe-uploader"
import OutfitGenerator from "@/components/outfit-generator"

export default function Dashboard() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-start p-24">
      <h1 className="text-4xl font-bold mb-8">Your Digital Wardrobe</h1>
      <div className="w-full max-w-4xl space-y-8">
        <WardrobeUploader />
        <OutfitGenerator />
      </div>
    </main>
  )
}

