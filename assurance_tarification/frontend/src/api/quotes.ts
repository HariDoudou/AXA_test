import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import ky from 'ky'

export interface QuoteSummary {
  id: number
  num_opportunite: string
  nom_client: string
  tarif_propose: string
  date_creation: string
}

export const useQuotes = () => {
  return useQuery({
    queryKey: ['quotes'],
    queryFn: async () => {
      const response = await ky.get(`${import.meta.env.VITE_API_URL}/api/devis/`)
      return response.json<QuoteSummary[]>()
    },
  })
}

export interface Quote {
  num_opportunite: string
  nom_client: string
  type_garantie: string
  type_bien: string
  type_travaux: string
  tarif_propose: number
  presence: boolean
  client_vip: boolean
  rcmo: boolean
  description: string
  adresse: Adresse
  taux_trc: number
  taux_do: number
}

interface Adresse {
  numero: string
  rue: string
  code_postal: string
  ville: string
}

export const useCreateQuote = () => {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: async (quote: Quote) => {
      const response = await ky.post(`${import.meta.env.VITE_API_URL}/api/devis/`, { json: quote })
      return response.json<QuoteSummary>()
    },
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ['quotes'],
      })
    },
  })
}
