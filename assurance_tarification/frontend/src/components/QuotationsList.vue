<script setup lang="ts">
import { useQuotes } from "@/api/quotes";
import ky from "ky";

const {data} = useQuotes()

<<<<<<< HEAD
const downloadFile = async(id: number, type: string) => {
  const response = await ky.get(`${import.meta.env.VITE_API_URL}/api/devis/${id}/export?type=${type}`)

  // Vérification de l'en-tête Content-Disposition
  const contentDisposition = response.headers.get('Content-Disposition');

  // Extraire le nom du fichier avec une expression régulière
  const matches = contentDisposition?.match(/filename="(.+)"/);
  const filename = matches ? matches[1] : `devis-${id}.${type === 'pdf' ? 'pdf' : 'docx'}`;

  // Créer un blob et générer un lien de téléchargement
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;

  // Encodage du nom de fichier pour le téléchargement
  const encodedFilename = encodeURIComponent(filename);
  link.setAttribute('download', encodedFilename);

  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(url);
}
=======
const downloadFile = async(id: number, type: string) =>{
  const response = await ky.get(`${import.meta.env.VITE_API_URL}/api/devis/${id}/export?type=${type}`)
  console.log(response.headers)

  const blob = await response.blob()
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url

  const filename = response.headers.get('Content-Disposition')?.split('filename=')[1]
  console.log(filename)
  const fileExtension = type === 'pdf' ? 'pdf' : 'docx'
  link.setAttribute('download', filename || `devis-${id}.${fileExtension}`)
  document.body.appendChild(link)
  link.click()
  link.remove()
  window.URL.revokeObjectURL(url)
}


>>>>>>> 23c61299005c76e4390916c8a20a70918a83672e
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Liste des Devis</h2>
    <table class="table-auto w-full border-collapse border border-gray-200">
      <thead>
        <tr class="bg-gray-100">
          <th class="border p-2">Numéro d'opportunité</th>
          <th class="border p-2">Nom du client</th>
          <th class="border p-2">Tarif proposé</th>
          <th class="border p-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="quote in data" :key="quote.id">
          <td class="border p-2">{{ quote.num_opportunite }}</td>
          <td class="border p-2">{{ quote.nom_client }}</td>
          <td class="border p-2">{{ quote.tarif_propose }} €</td>
          <td class="border p-2">
            <button class="px-4 py-2 bg-blue-500 text-white rounded" @click="downloadFile(quote.id, 'pdf')">📄 PDF
            </button>
<<<<<<< HEAD
            <button class="px-4 py-2 m-4 bg-blue-500 text-white rounded" @click="downloadFile(quote.id, 'word')">📝 Word </button>
=======
            <button class="px-4 py-2 bg-blue-500 text-white rounded" @click="downloadFile(quote.id, 'word')">📝 Word </button>
>>>>>>> 23c61299005c76e4390916c8a20a70918a83672e
          </td>
        </tr>
      </tbody>
    </table>
    <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded" @click="$emit('new-devis')">
      ➕ Nouveau devis
    </button>
  </div>
</template>
