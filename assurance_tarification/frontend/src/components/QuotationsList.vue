<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useQuotes } from "@/api/quotes";  // Assure-toi que `useQuotes` est bien configuré
import ky from "ky";  // Assure-toi que ky est installé pour les appels API

// Chargement des devis depuis l'API
const { data, isLoading, error } = useQuotes();

// Fonction pour télécharger un fichier (PDF ou Word)
const downloadFile = async (id: number, type: string) => {
  try {
    const response = await ky.get(`${import.meta.env.VITE_API_URL}/api/devis/${id}/export?type=${type}`);
    console.log(response.headers);

    // Créer un blob à partir de la réponse
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;

    // Extraire le nom du fichier depuis les en-têtes de la réponse
    const filename = response.headers.get("Content-Disposition")?.split("filename=")[1];
    console.log(filename);

    // Déterminer l'extension si nécessaire
    const fileExtension = type === "pdf" ? "pdf" : "docx";
    link.setAttribute("download", filename || `devis-${id}.${fileExtension}`);

    // Ajouter le lien, le cliquer pour télécharger le fichier, puis le supprimer
    document.body.appendChild(link);
    link.click();
    link.remove();

    // Révoquer l'URL pour libérer la mémoire
    window.URL.revokeObjectURL(url);
  } catch (err) {
    console.error("Erreur lors du téléchargement du fichier", err);
  }
};
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Liste des Devis</h2>

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
              class="px-4 py-2 bg-blue-500 text-white rounded"
              @click="downloadFile(quote.id, 'pdf')">
              📄 PDF
            </button>
            <button
              class="px-4 py-2 bg-blue-500 text-white rounded"
              @click="downloadFile(quote.id, 'word')">
              📝 Word
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Bouton pour créer un nouveau devis -->
    <button
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
      @click="$emit('new-devis')">
      ➕ Nouveau devis
    </button>
  </div>
</template>

<style scoped>
/* Quelques styles de base */
button {
  cursor: pointer;
}

button:hover {
  background-color: #3182ce;
}
</style>
