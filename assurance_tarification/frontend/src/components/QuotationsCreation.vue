<script setup lang="ts">
import { ref } from 'vue'
import ky from 'ky'
import { formOptions, useForm } from '@tanstack/vue-form'
import { Quote } from '@/api/quotes'

// Variables pour les champs du formulaire
const formOpts = formOptions({
  defaultValues: {
    num_opportunite: '',
    nom_client: '',
    type_garantie: '',
    type_bien: '',
    type_travaux: '',
    cout_ouvrage: '',
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
    tarif_trc: '',
    tarif_do: '',
  } as Quote,
})

const form = useForm({
  ...formOptions,
  onSubmit: async ({ value }) => {
    console.log(value)
  },
})
const garanties = ref([
  {
    label: 'DO seule',
    value: 'DO_seule',
  },
  {
    label: 'TRC seule',
    value: 'TRC_seule',
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
  <div class="flex flex-col gap-10 items-center">
    <h1>Création d'un devis</h1>

    <form
      class="flex flex-col gap-4"
      @submit="
        (e) => {
          e.preventDefault()
          e.stopPropagation()
          form.handleSubmit()
        }
      "
    >
      <div class="flex flex-row gap-4">
        <div class="flex flex-col gap-4 p-4">
          <form.Field name="num_opportunite">
            <template v-slot="{ field }">
              <UFormField label="Numéro d'opportunité">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="nom_client">
            <template v-slot="{ field }">
              <UFormField label="Nom du Client">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <div>
            <label class="block text-sm font-medium text-gray-700">Adresse</label>
            <div class="ml-4">
              <form.Field name="adresse.numero">
                <template v-slot="{ field }">
                  <UFormField label="Numéro : ">
                    <UInput
                      :name="field.name"
                      :modelValue="field.state.value"
                      @blur="field.handleBlur"
                      @update:modelValue="(value) => field.handleChange(value)"
                      class="w-full"
                    />
                  </UFormField>
                </template>
              </form.Field>

              <form.Field name="adresse.rue">
                <template v-slot="{ field }">
                  <UFormField label="Rue/Voie/Avenue : ">
                    <UInput
                      :name="field.name"
                      :modelValue="field.state.value"
                      @blur="field.handleBlur"
                      @update:modelValue="(value) => field.handleChange(value)"
                      class="w-full"
                    />
                  </UFormField>
                </template>
              </form.Field>

              <form.Field name="adresse.code_postal">
                <template v-slot="{ field }">
                  <UFormField label="Code postal : ">
                    <UInput
                      :name="field.name"
                      :modelValue="field.state.value"
                      @blur="field.handleBlur"
                      @update:modelValue="(value) => field.handleChange(value)"
                      class="w-full"
                    />
                  </UFormField>
                </template>
              </form.Field>

              <form.Field name="adresse.ville">
                <template v-slot="{ field }">
                  <UFormField label="Ville : ">
                    <UInput
                      :name="field.name"
                      :modelValue="field.state.value"
                      @blur="field.handleBlur"
                      @update:modelValue="(value) => field.handleChange(value)"
                      class="w-full"
                    />
                  </UFormField>
                </template>
              </form.Field>
            </div>
          </div>

          <form.Field name="description">
            <template v-slot="{ field }">
              <UFormField label="Description de l'ouvrage">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>
        </div>
        <div class="flex flex-col gap-4 p-4">
          <form.Field name="type_garantie">
            <template v-slot="{ field }">
              <UFormField label="Type de Garantie">
                <USelect
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  :items="garanties"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="type_bien">
            <template v-slot="{ field }">
              <UFormField label="Type de Bien">
                <USelect
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  :items="biens"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="type_travaux">
            <template v-slot="{ field }">
              <UFormField label="Type de Travaux">
                <USelect
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  :items="travaux"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="cout_ouvrage">
            <template v-slot="{ field }">
              <UFormField label="Coût de l'Ouvrage">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  trailing-icon="i-lucide-euro"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="presence">
            <template v-slot="{ field }">
              <UFormField label="Déjà existant ?">
                <UCheckbox
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="client_vip">
            <template v-slot="{ field }">
              <UFormField label="Client VIP ?">
                <UCheckbox
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="rcmo">
            <template v-slot="{ field }">
              <UFormField label="Voulez-vous la RCMO ?">
                <UCheckbox
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                />
              </UFormField>
            </template>
          </form.Field>
        </div>
        <div class="flex flex-col gap-4 p-4">
          <form.Field name="tarif_trc">
            <template v-slot="{ field }">
              <UFormField label="Taux TRC">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>

          <form.Field name="tarif_do">
            <template v-slot="{ field }">
              <UFormField label="Taux DO">
                <UInput
                  :name="field.name"
                  :modelValue="field.state.value"
                  @blur="field.handleBlur"
                  @update:modelValue="(value) => field.handleChange(value)"
                  class="w-full"
                />
              </UFormField>
            </template>
          </form.Field>
        </div>
      </div>
      <div>
        <h1>Tarification</h1>
        <div class="flex-row gap-4 grid grid-cols-3 p-4">
          <label> Tarif TRC : </label>
          <label> Tarif DO : </label>
          <label> Tarif Duo : </label>
        </div>
        <h1>Prime totale :</h1>
      </div>
      <div class="flex flex-col items-center">
        <form.Subscribe>
          <template v-slot="{ canSubmit, isSubmitting }">
            <UButton type="submit" :disabled="!canSubmit">
              {{ isSubmitting ? '...' : 'Submit' }}
            </UButton>
          </template>
        </form.Subscribe>
      </div>
    </form>
  </div>
</template>
