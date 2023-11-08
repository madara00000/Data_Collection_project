<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  background-color: #f8f8f8;  
  padding: 20px;  
  min-height: 100vh;  
  display: flex;
  flex-direction: column;
  align-items: center;
}
 
router-view {
  width: 100%;  
  max-width: 800px;  
  background-color: #ffffff;  
  padding: 20px;  
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);  
  border-radius: 8px;  }
 
</style>
