<script setup lang="ts">
import { reactive, ref } from 'vue'
import { Quote, useCreateQuote } from '@/api/quotes'
import { FormSubmitEvent } from '@nuxt/ui/dist/module'
const mutation = useCreateQuote()
const state = reactive<Quote>({
  num_opportunite: '',
  nom_client: '',
  type_garantie: '',
  type_bien: '',
  type_travaux: '',
  tarif_propose: 0,
  presence: false,
  client_vip: false,
  rcmo: false,
  description: '',
  adresse: {
    numero: '',
    rue: '',
    code_postal: '',
    ville: '',
  },
  taux_trc: 0,
  taux_do: 0,
})
// Variables pour les champs du formulaire
const onSubmit = async (event: FormSubmitEvent<Quote>) => {
  console.log(event.data)
  mutation.mutate(event.data)
}

const garanties = ref([
  {
    label: 'DO seule',
    value: 'DO',
  },
  {
    label: 'TRC seule',
    value: 'TRC',
  },
  {
    label: 'DO + TRC',
    value: 'DO_TRC',
  },
])

const biens = ref([
  {
    label: 'Habitation',
    value: 'Habitation',
  },
  {
    label: 'Hors habitation',
    value: 'Hors_habitation',
  },
])

const travaux = ref([
  {
    label: 'Ouvrage neuf',
    value: 'Ouvrage_neuf',
  },
  {
    label: 'Rénovation légère',
    value: 'Renovation_legere',
  },
  {
    label: 'Rénovation lourde',
    value: 'Renovation_lourde',
  },
])
</script>

<template>
  <div class="p-4 flex flex-col gap-4 items-center">
    <h1 class="text-2xl font-bold mb-4">Créer un Devis</h1>
    <UButton to="/"> Liste des devis </UButton>
  </div>
  <div class="p-4 flex flex-col gap-4 items-center">
    <p class="text-gray-600 mb-4">
      Remplissez les informations ci-dessous pour créer un nouveau devis.
    </p>
  </div>

  <UForm :state="state" @submit="onSubmit" class="grid grid-cols-3 gap-8 min-w-64">
    <div class="flex flex-col gap-4">
      <h2 class="text-xl font-bold mb-4">Informations sur le client</h2>
      <UFormField label="Numéro d'opportunité" name="num_opportunite">
        <UInput v-model="state.num_opportunite" class="w-full" />
      </UFormField>

      <UFormField label="Nom du Client" name="nom_client">
        <UInput v-model="state.num_opportunite" class="w-full" />
      </UFormField>

      <UFormField label="Adresse" name="adresse">
        <div class="flex flex-col gap-2 ml-8">
          <UFormField label="Numéro"
            ><UInput v-model="state.adresse.numero" class="w-full"
          /></UFormField>

          <UFormField label="Rue/Voie/Avenue"
            ><UInput v-model="state.adresse.rue" class="w-full"
          /></UFormField>
          <UFormField label="Code Postal"
            ><UInput v-model="state.adresse.code_postal" class="w-full"
          /></UFormField>
          <UFormField label="Ville"
            ><UInput v-model="state.adresse.ville" class="w-full"
          /></UFormField>
        </div>
      </UFormField>
    </div>
    <div class="flex flex-col gap-4">
      <h2 class="text-xl font-bold mb-4">Informations sur le projet</h2>
      <UFormField label="Description de l'ouvrage" name="description">
        <UInput v-model="state.description" class="w-full" />
      </UFormField>
      <UFormField label="Type de Garantie" name="type_garantie">
        <USelect v-model="state.type_garantie" :items="garanties" class="w-full" />
      </UFormField>

      <UFormField label="Type de Bien" name="type_bien">
        <USelect v-model="state.type_bien" :items="biens" class="w-full" />
      </UFormField>

      <UFormField label="Type de Travaux" name="type_travaux">
        <USelect v-model="state.type_travaux" :items="travaux" class="w-full" />
      </UFormField>

      <UFormField label="Coût de l'Ouvrage" name="tarif_propose">
        <UInput v-model="state.tarif_propose" class="w-full" trailing-icon="i-lucide-euro" />
      </UFormField>

      <UFormField label="Déjà existant ?" name="presence">
        <UCheckbox v-model="state.presence" />
      </UFormField>

      <UFormField label="Client VIP ?" name="client_vip">
        <UCheckbox v-model="state.client_vip" />
      </UFormField>

      <UFormField label="Voulez-vous la RCMO ?" name="rcmo">
        <UCheckbox v-model="state.rcmo" />
      </UFormField>
    </div>
    <div class="flex flex-col gap-4">
      <h2 class="text-xl font-bold mb-4">Informations sur les taux</h2>
      <UFormField label="Taux TRC" name="taux_trc">
        <UInput v-model="state.taux_trc" class="w-full" />
      </UFormField>

      <UFormField label="Taux DO" name="taux_do">
        <UInput v-model="state.taux_do" class="w-full" />
      </UFormField>
      <div class="pt-6">
        <h2 class="text-l font-bold mb-4">Tarifications</h2>

        <div class="flex-col gap-4 flex">
          <label>
            Tarif TRC :
            {{ state.taux_trc * state.tarif_propose }} €
          </label>
          <label> Tarif DO : {{ state.taux_do * state.tarif_propose }} €</label>
          <label>
            Tarif Duo :
            {{ state.taux_trc * state.tarif_propose + state.taux_do * state.tarif_propose }}
            €</label
          >
          <label class="text-lg pt-14">
            Prime totale :
            {{ state.taux_trc * state.tarif_propose + state.taux_do * state.tarif_propose }} €
          </label>
        </div>
      </div>
    </div>
  </UForm>
  <div class="pt-10 flex flex-col gap-4 items-center">
    <UFormField>
      <UButton type="submit">Valider</UButton>
    </UFormField>
  </div>
</template>
