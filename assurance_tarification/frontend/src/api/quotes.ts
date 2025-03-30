import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import ky from 'ky'
import * as v from 'valibot'

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

export const schema = v.object({
  adresse: v.object({
    numero: v.pipe(v.string(), v.regex(/^[A-Za-z0-9]+$/)),
    rue: v.pipe(v.string(), v.regex(/^[A-Za-z0-9]+$/)),
    code_postal: v.pipe(
      v.string(),
      v.regex(/^[0-9]*$/),
      v.minLength(5, '5 caractères obligatoires'),
      v.maxLength(5, '5 caractères obligatoires'),
    ),
    ville: v.pipe(v.string(), v.regex(/^[A-Za-z]+$/)),
  }),
  num_opportunite: v.pipe(v.string(), v.regex(/^[A-Za-z0-9]+$/)),
  nom_client: v.pipe(v.string(), v.regex(/^[A-Za-z0-9]+$/)),
  description: v.pipe(v.string(), v.regex(/^[A-Za-z0-9]+$/)),
  tarif_propose: v.number(),
  type_garantie: v.picklist(['', 'DO', 'TRC', 'DO_TRC']),
  type_bien: v.picklist(['', 'Habitation', 'Hors_habitation']),
  type_travaux: v.picklist(['', 'Ouvrage_neuf', 'Renovation_legere', 'Renovation_lourde']),
  presence: v.boolean(),
  client_vip: v.boolean(),
  rcmo: v.boolean(),
  taux_trc: v.number(),
  taux_do: v.number(),
})

export type Quote = v.InferOutput<typeof schema>

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
