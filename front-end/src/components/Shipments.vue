<template>
  <div class="shipments">
    <b-button v-b-modal.create class="m-2">Create Shipment</b-button>
    <b-table
      striped
      hover
      :items="shipments"
      :fields="fields"
    >
      <template #cell(actions)="data">
        <b-dropdown text="Options" variant="outline-danger">
          <b-dropdown-item @click="editShipment(data.item)">Edit</b-dropdown-item>
          <b-dropdown-item @click="deleteShipment(data.item.id)">Delete</b-dropdown-item>
        </b-dropdown>
      </template>
    </b-table>
    <create-update-shipment-modal mode="create" @submit="getShipments" />
    <create-update-shipment-modal mode="update" :shipment="shipmentToUpdate"  @submit="getShipments" />
  </div>
</template>

<script>
import CreateUpdateShipmentModal from "./CreateUpdateShipmentModal.vue";
export default {
    name: "Shipments",
    components: { CreateUpdateShipmentModal },
    data() {
        return {
            shipments: [],
            shipmentToUpdate: {},
            fields: [
                "id",
                "shipping_address",
                "biling_address",
                "product_price",
                "delivery_cost",
                "final_price",
                "actions"
            ],
        };
    },
    mounted() {
        this.getShipments();
    },
    methods: {
        getShipments() {
          console.log('get');
          this.axios.get("api/shipments/")
            .then((res) => {
              console.log(res);
              this.shipments = res.data;
            }).catch(err => {
                console.log(err);
            });
        },
        editShipment(item) {
          this.shipmentToUpdate = JSON.parse(JSON.stringify(item))
          this.$bvModal.show('update')
        },
        deleteShipment(id) {
            this.axios.delete(`api/shipments/${id}/`).finally(this.getShipments)
        }
    },
}
</script>
<style scoped>

</style>
