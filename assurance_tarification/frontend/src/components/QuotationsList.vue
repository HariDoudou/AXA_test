<script setup lang="ts">
import { useQuotes, QuoteSummary } from '@/api/quotes'
import { TableColumn } from '@nuxt/ui/dist/module'
import { downloadFile } from '@/utils'
import { h, ref, resolveComponent } from 'vue'
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
    cell: ({ row }) => `${row.getValue('tarif_propose')} €`,
  },
  { id: 'action', header: 'Actions' },
]

const globalFilter = ref('')
</script>

<template>
  <div class="p-4">
    <div class="flex flex-row justify-between items-center">
      <h2 class="text-2xl font-bold mb-4">Liste des Devis</h2>
    </div>
    <div class="border-gray-200 border-solid border-2 rounded-2xl">
      <div class="flex flex-row items-center px-2 py-4 border-solid border-gray-200 border-b-2">
        <UButton to="/create" icon="i-lucide-plus"> Nouveau </UButton>
        <div class="flex-1"></div>
        <UInput
          v-model="globalFilter"
          class="max-w-sm"
          placeholder="Rechercher..."
          icon="i-lucide-search"
        />
      </div>
      <!-- Table pour afficher les devis -->
      <UTable
        class="flex"
        :data="data"
        :loading="isLoading"
        :columns="columns"
        v-model:global-filter="globalFilter"
      >
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
  </div>
</template>
