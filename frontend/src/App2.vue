<template>
    <div id="app-3">

        <toggle-button 
            name="LEBOUTON"
            :value="true"
            :labels="{checked: 'Activate', unchecked: 'Deactivate'}"
            :width="100"
            :color="{checked: 'indigo', unchecked: 'pink'}"
            />

    </div>
</template>

<script>

import ToggleButton from 'vue-js-toggle-button'

export default {

    
    name: "app-3",

};
</script>