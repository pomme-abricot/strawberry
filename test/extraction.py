from openalea.deploy.shared_data import shared_data
import openalea.strawberry
from openalea.mtg.io import read_mtg_file
from openalea.mtg.algo import union

from openalea.strawberry.variables import extract_at_module_scale, extract_at_node_scale, extract_at_plant_scale

def test_extract_at_module_scale(self):
    files = shared_data(openalea.strawberry).glob('*.mtg')
    mtg_path = dict((f.namebase, f) for f in files)
    mtg1 = read_mtg_file(mtg_path[list(mtg_path)[0]])
    mtg2 = read_mtg_file(mtg_path[list(mtg_path)[1]])
    mtg = union(mtg1, mtg2)
    genotype = mtg_path[list(mtg_path)[0]].namebase

    genotypes = mtg.property('Genotype')
    clery_vids=[vid for vid in mtg.vertices(scale=1) if genotypes.get(vid) == genotype]

    df = extract_at_module_scale(mtg, clery_vids)

    assert not df.empty
    assert set(df['Genotype']) == {genotype}


