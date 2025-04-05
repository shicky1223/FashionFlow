import RegisterForm from "@/components/register-form"

export default function Register() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">Register</h1>
      <RegisterForm />
    </main>
  )
}

