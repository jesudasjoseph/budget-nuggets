<script lang="ts">
	import { authenticatedAPICall } from '../../api/util';
	let text: any;

	function getAccounts() {
		authenticatedAPICall('GET', 'accounts/').then((response) => {
			if (response) {
				if (response.status === 200) {
					text = response.json();
				} else if (response.status === 204) {
					text = 'No Accounts found!';
					console.log(response);
				}
			}
		});
	}
</script>

<button on:click={getAccounts}>Click</button>
{text}
