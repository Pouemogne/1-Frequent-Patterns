from typing import Set, List

from classes.dataset import Dataset
from classes.itemset import Itemset
from classes.item import Item
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts
from classes.sorted_dataset import SortedDataset
from classes.sorted_transaction import SortedTransaction
from classes.item_tuple import ItemTuple
from classes.fp_tree import FPTree
from classes.conditional_pattern_base import ConditionalPatternBase
from classes.conditional_pattern import ConditionalPattern


class FPgrowth:
    def __init__(self, min_support: int = 2):
        """
        Initialize the FP-growth algorithm with the a minimum (absolute) support.

        Parameters:
        min_support (int): The minimum (absolute) support. This parameter defines the minimum number
                           of occurrences an itemset must have to be considered frequent. Must be a positive integer.
                           Default value is 2.
        """
        # Ensure that the minimum support is a positive integer
        if not isinstance(min_support, int) or min_support < 1:
            raise ValueError("The minimum support must be a positive integer.")

        self.min_support = min_support
        self.frequent_itemsets = set()

    def _generate_frequent_one_itemsets_with_occurrence_counts(
        self, dataset: Dataset
    ) -> ItemsetsWithOccurrenceCounts:
        itemsets_with_occcurence_counts = {}
        for transaction in dataset.transaction:
            for item in transaction:
                itemset= frozenset([item])
                if itemset in itemsets_with_occurence_counts:
                    itemsets_with_occurence_counts[itemset]+=1
                else:
                    itemsets_with_occurence_counts[itemset]=1

        frequent_one_itemsets={
            Itemset(itemset):count
            for itemset,count in itemsets_with_occurence_counts.items()
            if count>=self.min_support
        }
       
        return  ItemsetsWithOccurenceCounts (frequent_one_itemsets)      
            
        
        """
        Generate all frequent 1-itemsets for the given dataset.

        Parameters:
        dataset (Dataset): The dataset for which the frequent 1-itemsets should be generated.

        Returns:
        ItemsetsWithOccurrenceCounts: A dictionary containing the frequent 1-itemsets as keys and their occurrence counts as values.
        """
        # TODO

    def _generate_f_list(
        self, frequent_one_itemsets: ItemsetsWithOccurrenceCounts
    ) -> List[Itemset]:
        f_list= sorted(frequent_one_itemsets.itemsets, key=lambda x: -frequent_one_itemsets.itemsets[x])
        return f_list
            
        """
        Generate the f-list for the given frequent 1-itemsets.

        Parameters:
        frequent_one_itemsets (ItemsetsWithOccurrenceCounts): The frequent 1-itemsets with their occurrence counts for which the F-list should be generated.

        Returns:
        List[Itemset]: A f-list containing the frequent 1-itemsets sorted by decreasing occurrence count.
        """
        # TODO

    def _sort_dataset_according_to_f_list(
        self, dataset: Dataset, f_list: List[Itemset]
    ) -> SortedDataset:
        item_index= {itemset.items: index for index, itemset in enumerate( f_list)}
        sorted_transaction=[]
        for transaction in dataset.transactions:
            sorted_transaction=sorted(transaction, key=lambda item: item_index[frosenset([item])])
            sorted_transactions.append(sorted_transaction(sorted_transaction))
                     
        sorted_dataset= SortedDataset(sorted_transactions)
        return sorted_dataset
        """
        Sort the dataset according to the given f-list.

        Parameters:
        dataset (Dataset): The dataset to be sorted.
        f_list (List[Itemset]): The f-list according to which the dataset should be sorted.

        Returns:
        SortedDataset: The sorted dataset.
        """
        # TODO

    def _construct_initial_fp_tree(self, sorted_dataset: SortedDataset) -> FPTree:
        initial_fp_tree = FPTree()
        root=fp_tree.root
        for transaction in sorted_dataset.transactions:
            current_node= root
            for item in transaction:
                if item in current_node.children:
                    current_node.children[item].count +=1
                else:
                    new_node= FPTreeNode(item,1)
                    currnet_node.children[item]=new_node
                    new_node.parent=current_node

                    if item in fp_tree.header_table:
                        initial_fp_tree.header_table[item].append(new_node)
                    else:
                        initial_fp_tree.header_table[item]=[new_node]

        return initial_fp_tree

        
        """
        Construct the initial FP-tree from the given sorted dataset.

        Parameters:
        sorted_dataset (SortedDataset): The sorted dataset from which the initial FP-tree should be constructed.

        Returns:
        FPTree: The initial FP-tree.
        """
        # TODO

    def _get_conditional_pattern_base(
        self, item: Item, fp_tree: FPTree
    ) -> ConditionalPatternBase:
        conditional_pattern_base=[]

        nodes=fp_tree.header_table.get(item,[])

        for node in nodes:
            path=[]
            current_node=node.parent
            while current_node and current_node.item is not None:
                path.append(currnet_node.item)
                current_node=current_node.parent
            if path:
                path.reverse()
                conditional_pattern_base.append(cConditionalPattren(path, node.count))
    return ConditionalPatternBase(conditional_pattern_base)
        
        """
        Get the conditional pattern base for the given item in the FP-tree.

        Parameters:
        item (Item): The item for which the conditional pattern base should be generated.
        fp_tree (FPTree): The FP-tree from which the conditional pattern base should be extracted.

        Returns:
        ConditionalPatternBase: The conditional pattern base for the given item.
        """
        # TODO

    def _construct_conditional_fp_tree(
        self, conditional_pattern_base: ConditionalPatternBase
    ) -> FPTree:

        conditional_fp_tree= FPTree()

        for pattern in conditional_pattern_base.patterns:
            path,count= pattern.path, pattern.count
            current_node= conditional_fp_tree.root
            for item in path: 
                if item in current_node.children:
                    current_node.children[item].count+=count
                else:
                    new_node=FPTreeNode(item,count)
                    current_node.childre[item]=current_node
                    if item in conditional_fp_tre.header_table:
                        conditional_fp_tree.header_table[item].append(new_node)
                    else:
                        conditional_fp_tree.tree.header_table[item]
                current_node=current_node.children[item]
        return conditional_fp_tree
                
        """
        Construct a conditional FP-tree from the given sorted dataset.

        Parameters:
        conditional_pattern_base (ConditionalPatternBase): The conditional pattern base for which the conditional FP-tree should be constructed.

        Returns:
        FPTree: The conditional FP-tree.
        """
        # TODO

    def fit(self, dataset: Dataset):
        frequent_one_itemsets=self._generate_frequent_one_itemsets_with_occurrence_counts(dataset)
        f_list= self._generate_f_list(frequent_one_itemsets)
        sorted_dataset = self._sort_dataset_according_to_f_list(dataset, f_list)
        fp_tree = self._construct_initial_fp_tree(sorted_dataset)
        self.frequent_itemsets = set(frequent_one_itemsets.itemsets.keys())
        """
        Use the FP-growth algorithm to find all frequent itemsets in the given dataset.
        Saves the frequent itemsets in the frequent_itemsets attribute.

        Parameters:
        dataset (Dataset): The dataset to which the FP-growth algorithm should be fitted.
        """
        # TODO
