import { reactive } from "vue";

// These are the values which will be used between different components
export const store = reactive({
    items: [],
    fetchingData: true,
    savedRecipe: []
})