<script setup lang="ts">
import { useQuotes } from "@/api/quotes";

const {data} = useQuotes()
</script>

<template>
  <div>
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
          <!-- <td class="border p-2">
            <a :href="quote.document_pdf" class="text-blue-500" target="_blank">📄 PDF</a>
            &nbsp;|&nbsp;
            <a :href="quote.document_word" class="text-blue-500" target="_blank">📝 Word</a>
          </td> -->
        </tr>
      </tbody>
    </table>
    <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded" @click="$emit('new-devis')">
      ➕ Nouveau devis
    </button>
  </div>
</template>
