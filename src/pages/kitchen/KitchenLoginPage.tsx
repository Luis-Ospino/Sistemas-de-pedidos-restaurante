import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ENV } from '@/api/env'
import { setKitchenToken } from '@/store/kitchenAuth'
import { SectionTitle } from '@/components/SectionTitle'

export function KitchenLoginPage() {
  const navigate = useNavigate()
  const [pin, setPin] = useState('')
  const [error, setError] = useState('')

  function submit() {
    if (pin !== ENV.KITCHEN_PIN) {
      setError('PIN de cocina invalido')
      return
    }
    const token = ENV.KITCHEN_FIXED_TOKEN || pin
    setKitchenToken(token)
    setError('')
    navigate('/kitchen/board', { replace: true })
  }

  return (
    <div className="space-y-6">
      <SectionTitle
        title="Cocina"
        subtitle="Ingresa el PIN para habilitar acciones de cocina."
      />

      <div className="card space-y-4 p-6">
        <label className="block text-sm text-slate-300" htmlFor="kitchen-pin">
          PIN de cocina
        </label>
        <input
          id="kitchen-pin"
          type="password"
          value={pin}
          onChange={(e) => setPin(e.target.value)}
          className="w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-2 text-slate-100"
          placeholder="Ingresa PIN"
        />
        {error ? <div className="text-sm text-rose-400">{error}</div> : null}
        <div className="flex items-center justify-end">
          <button className="btn btn-primary cursor-pointer" onClick={submit}>
            Entrar a cocina
          </button>
        </div>
      </div>
    </div>
  )
}
