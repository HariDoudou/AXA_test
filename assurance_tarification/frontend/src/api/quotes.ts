import { useQuery } from "@tanstack/vue-query"
import ky from "ky"

interface Quote {
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
      return response.json<Quote[]>()
    },
  })
}
