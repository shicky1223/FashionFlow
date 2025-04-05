import LoginForm from "@/components/login-form"

export default function Login() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">Login</h1>
      <LoginForm />
    </main>
  )
}

