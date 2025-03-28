<script setup lang="ts">
import { ref, onMounted } from "vue";
import { RouterLink} from "vue-router";
import { useQuotes } from "@/api/quotes";
import ky from "ky";

const { data, isLoading, error } = useQuotes();

const downloadFile = async (id: number, type: string) => {
  try {
    const response = await ky.get(`${import.meta.env.VITE_API_URL}/api/devis/${id}/export?type=${type}`);
    console.log(response.headers);

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    const filename = response.headers.get("Content-Disposition")?.split("filename=")[1];
    console.log(filename);

    const fileExtension = type === "pdf" ? "pdf" : "docx";
    link.setAttribute("download", filename || `devis-${id}.${fileExtension}`);
    document.body.appendChild(link);
    link.click();
    link.remove();

    window.URL.revokeObjectURL(url);
  } catch (err) {
    console.error("Erreur lors du téléchargement du fichier", err);
  }
};
</script>

<template>
  <div class="p-4">
    <div class="flex flex-row justify-between items-center">
      <h2 class="text-2xl font-bold mb-4">Liste des Devis</h2>
      <RouterLink
        class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        to="/create">
        ➕ Nouveau devis
      </RouterLink>
    </div>


    <!-- Table pour afficher les devis -->
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
            <!-- Boutons pour télécharger le devis en PDF ou Word -->
            <button
              class="px-4 py-2 mx-2 bg-blue-500 text-white rounded"
              @click="downloadFile(quote.id, 'pdf')">
              📄 PDF
            </button>
            <button
              class="px-4 py-2 mx-2 bg-blue-500 text-white rounded"
              @click="downloadFile(quote.id, 'word')">
              📝 Word
            </button>
          </td>
        </tr>
      </tbody>
    </table>


  </div>
</template>
