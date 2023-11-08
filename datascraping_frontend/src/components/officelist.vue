<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable-next-line no-unused-vars -->
<template>
  <div class="container mt-4">
    <h1 class="display-4 mb-4">Technology & Communication companies in Morroco</h1>
    <div class="custom-card-text"> Theese are some companies and offices related to 
     Computer Service/ Repair/
     IT Companies/
     Web Development companies/
     Internet service providers/
     Computer Networking and Management/
     Digital Marketing agencies/
     Mobile App Development companies/
     Branding agencies/
     IT Consultancies/
     Web Hosting companies/
     Robotics and AI/
     Electronics Companies/
     Security systems and Access control/
     Printer services and installation. </div><br>
    <div class="row">
      <div class="col-md-6" v-for="office in officeList" :key="office.id">
        <div class="custom-card mb-4">
          <div class="custom-card-body">
            <h2 class="custom-card-title">{{ office.name }}</h2>
          <div class="custom-card-text"> 
            <p>Industry: {{ office.industry }}</p>
            <p>Phone: {{ office.mobile }}</p>
            <p>Landline phone number: {{ office.landlinemobile }}</p>
            <p>Address: {{ office.address }}</p>
            <p>Email: {{ office.email }}</p></div>  
          </div>
         

          <div class="custom-card-footer">
            <a target="_blank" :href="office.link " class="custom-btn">Check their website !</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      officeList: [], // Initialize an empty array to store office details
    };
  },

  created() {
    // When the component is created, fetch all offices
    this.fetchAllOffices();
  },

  methods: {
    fetchAllOffices() {
      // Make an API request to fetch all offices
      axios
        .get(`http://localhost:3000/get-data`)
        .then((response) => {
          console.log(response.data);
 
          this.officeList = response.data;
        })
        .catch((error) => {
          console.error('Error at fetching offices:', error);
        });
    },
  },
};
</script>

<style scoped>
 .custom-card {
  border: 2px solid #007bff;  
  transition: transform 0.2s;  
  background-color: #fff;  
  margin-bottom: 20px;
  padding: 15px;
  border-radius: 5px;
}

.custom-card:hover {
  transform: scale(1.02);  
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);  
  background-color: #67b0ff;
}

.custom-card-title {
  font-size: 24px;
  color: #333; 
}

.custom-card-text {
  font-size: 16px;
  color: #555;  
}

.custom-card-footer {
  
  text-align: center;
}

.custom-btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff;  
  color: #fff;  
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.2s;
}

.custom-btn:hover {
  background-color: #0056b3; 
}
</style>
