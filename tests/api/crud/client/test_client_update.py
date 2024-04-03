from pathlib import Path

import pytest
from httpx import AsyncClient
from starlette import status

from tests.const import URLS

BASE_DIR = Path(__file__).parent
FIXTURES_PATH = BASE_DIR / 'fixtures'


@pytest.mark.parametrize(
    ('username', 'password', 'first_name', 'last_name', 'company_name', 'client_id', 'expected_status', 'fixtures'),
    [
        (
            'user',
            'qwerty',
            'Ivan',
            'Not_Russkiy',
            'Sirius',
            2,
            status.HTTP_200_OK,
            [
                FIXTURES_PATH / 'sirius.client.json',
                FIXTURES_PATH / 'sirius.user.json',
            ],
        ),
    ],
)

@pytest.mark.asyncio()
@pytest.mark.usefixtures('_common_api_fixture')
async def test_update_client(
    client: AsyncClient,
    first_name: str,
    last_name: str,
    company_name: str,
    client_id: int,
    expected_status: int,
    access_token: str,
) -> None:
    response = await client.post(
        URLS['client']['update'].format(client_id=client_id),
        json={'first_name': first_name, 'last_name': last_name, 'company_name': company_name},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == expected_status
