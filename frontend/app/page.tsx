import Link from "next/link"
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">AI Wardrobe Assistant</h1>
      <div className="space-y-4">
        <Link href="/login">
          <Button className="w-full">Login</Button>
        </Link>
        <Link href="/register">
          <Button className="w-full" variant="outline">
            Register
          </Button>
        </Link>
      </div>
    </main>
  )
}

