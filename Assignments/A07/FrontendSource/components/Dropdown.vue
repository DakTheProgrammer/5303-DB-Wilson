<template>
  <span id = 'dd'>
        <label for='semester'>Semester:</label>
        <select name='semester' v-model="selected" @change="SendText()">
            <option value="spring 2022">spring 2022</option>
            <option value="fall 2021">fall 2021</option>
            <option value="summer1 2021">summer1 2021</option>
            <option value="summer2 2021">summer2 2021</option>
            <option value="spring 2021">spring 2021</option>
            <option value="a" hidden disabled>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</option>
        </select>
  </span>
</template>

<script>

export default {
  data(){
    return{
      selected: "spring 2022"
    }
  },
  methods:{
    SendText(){
      this.$emit('getDropdown', this.selected)
    }
  }
}
</script>

<style>
#dd
{
  position: relative;
  right: 48px;
}
</style>
