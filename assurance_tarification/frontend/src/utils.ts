import ky from 'ky'
import { QuoteSummary } from './api/quotes'
import dayjs from 'dayjs'

export const downloadFile = async (
  id: number,
  type: 'word' | 'pdf',
  data: QuoteSummary[] | undefined | QuoteSummary,
) => {
  if (!data) {
    return
  }

  try {
    const response = await ky.get(
      `${import.meta.env.VITE_API_URL}/api/devis/${id}/export?type=${type}`,
    )
    console.log(response.headers)

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)

    const link = document.createElement('a')
    link.href = url
    const filename = response.headers.get('Content-Disposition')?.split('filename=')[1]
    console.log(filename)

    const fileExtension = type === 'pdf' ? 'pdf' : 'docx'
    const devis = Array.isArray(data) ? data.find((d) => d.id === id) : data
    const formatDate = dayjs(devis?.date_creation).format('DD-MM-YYYY:HH:mm')
    const defaultName = devis
      ? `Proposition_commerciale_${devis.num_opportunite}_${formatDate}.${fileExtension}`
      : `Proposition_commerciale.${fileExtension}`
    link.setAttribute('download', filename || defaultName)
    document.body.appendChild(link)
    link.click()
    link.remove()

    window.URL.revokeObjectURL(url)
  } catch (err) {
    console.error('Erreur lors du téléchargement du fichier', err)
  }
}
