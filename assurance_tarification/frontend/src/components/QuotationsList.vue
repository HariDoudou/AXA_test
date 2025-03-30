<script setup lang="ts">
import { useQuotes, QuoteSummary } from '@/api/quotes'
import { TableColumn } from '@nuxt/ui/dist/module'
import { downloadFile } from '@/utils'
import { h, resolveComponent } from 'vue'
import { Column } from '@tanstack/vue-table'
const UButton = resolveComponent('UButton')

const { data, isLoading, error } = useQuotes()

const columnSorting = (column: Column<QuoteSummary, unknown>, label: string) => {
  const isSorted = column.getIsSorted()

  return h(UButton, {
    color: 'neutral',
    variant: 'ghost',
    label,
    icon: isSorted
      ? isSorted === 'asc'
        ? 'i-lucide-arrow-up-narrow-wide'
        : 'i-lucide-arrow-down-wide-narrow'
      : 'i-lucide-arrow-up-down',
    class: '-mx-2.5',
    onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
  })
}

const columns: TableColumn<QuoteSummary>[] = [
  {
    accessorKey: 'num_opportunite',
    header: ({ column }) => columnSorting(column, `N° d'opportunité`),
  },
  {
    accessorKey: 'nom_client',
    header: ({ column }) => columnSorting(column, 'Nom du client'),
  },
  {
    accessorKey: 'tarif_propose',
    header: ({ column }) => columnSorting(column, 'Tarif proposé'),
  },
  { id: 'action', header: 'Actions' },
]
</script>

<template>
  <div class="p-4">
    <div class="flex flex-row justify-between items-center">
      <h2 class="text-2xl font-bold mb-4">Liste des Devis</h2>
      <UButton to="/create"> ➕ Nouveau devis </UButton>
    </div>

    <!-- Table pour afficher les devis -->
    <UTable :data="data" :loading="isLoading" :columns="columns" class="flex-1">
      <template #action-cell="{ row }">
        <div class="flex flex-row gap-2">
          <UTooltip text="Export on pdf file">
            <UButton
              icon="i-teenyicons-pdf-outline"
              @click="downloadFile(row.original.id, 'pdf', data)"
            />
          </UTooltip>
          <UTooltip text="Export on word file">
            <UButton
              icon="i-teenyicons-ms-word-outline"
              @click="downloadFile(row.original.id, 'word', data)"
            />
          </UTooltip>
        </div>
      </template>
    </UTable>
  </div>
</template>
